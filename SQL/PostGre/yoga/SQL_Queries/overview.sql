-- Monthly Financial Overview for Tarifa Yoga (2026)
-- Calculates Profit after IVA (21%), IRPF (20%), and Deductible Expenses

WITH monthly_income AS (
    -- Aggregate Gross Income from Package sales per month
    SELECT 
        EXTRACT(MONTH FROM purchase_date) as month,
        SUM(price_paid) as gross_income
    FROM core_package
    WHERE EXTRACT(YEAR FROM purchase_date) = 2026
    GROUP BY 1
),
monthly_expenses AS (
    -- Aggregate Expenses per month, grouping by Deducible vs Social Security
    SELECT 
        EXTRACT(MONTH FROM date) as month,
        SUM(CASE WHEN category = 'SOCIAL' THEN amount ELSE 0 END) as social_security,
        SUM(CASE WHEN category NOT IN ('SOCIAL', 'TAX') THEN amount ELSE 0 END) as deductible_expenses
    FROM core_expense
    WHERE EXTRACT(YEAR FROM date) = 2026
    GROUP BY 1
)
SELECT 
    TO_CHAR(TO_DATE(COALESCE(i.month, e.month)::text, 'MM'), 'Month') as month_name,
    COALESCE(i.gross_income, 0) as gross_income_iva_incl,
    -- IVA Calculation: Gross / 1.21 = Base. IVA = Gross - Base.
    ROUND(COALESCE(i.gross_income, 0) - (COALESCE(i.gross_income, 0) / 1.21), 2) as iva_collected,
    -- Net Revenue (Base Imponible)
    ROUND(COALESCE(i.gross_income, 0) / 1.21, 2) as net_revenue,
    COALESCE(e.deductible_expenses, 0) as expenses,
    COALESCE(e.social_security, 0) as social_security,
    -- Operating Profit = Net Revenue - (Expenses + Soc. Sec)
    ROUND((COALESCE(i.gross_income, 0) / 1.21) - (COALESCE(e.deductible_expenses, 0) + COALESCE(e.social_security, 0)), 2) as operating_profit,
    -- IRPF: 20% of Operating Profit (if positive)
    CASE 
        WHEN (COALESCE(i.gross_income, 0) / 1.21) - (COALESCE(e.deductible_expenses, 0) + COALESCE(e.social_security, 0)) > 0 
        THEN ROUND(((COALESCE(i.gross_income, 0) / 1.21) - (COALESCE(e.deductible_expenses, 0) + COALESCE(e.social_security, 0))) * 0.20, 2)
        ELSE 0
    END as irpf_advance,
    -- Final Net Profit (Profit after all taxes and expenses)
    ROUND(
        ((COALESCE(i.gross_income, 0) / 1.21) - (COALESCE(e.deductible_expenses, 0) + COALESCE(e.social_security, 0))) - 
        CASE 
            WHEN (COALESCE(i.gross_income, 0) / 1.21) - (COALESCE(e.deductible_expenses, 0) + COALESCE(e.social_security, 0)) > 0 
            THEN ((COALESCE(i.gross_income, 0) / 1.21) - (COALESCE(e.deductible_expenses, 0) + COALESCE(e.social_security, 0))) * 0.20
            ELSE 0
        END, 2
    ) as final_net_profit
FROM monthly_income i
FULL OUTER JOIN monthly_expenses e ON i.month = e.month
ORDER BY COALESCE(i.month, e.month);
