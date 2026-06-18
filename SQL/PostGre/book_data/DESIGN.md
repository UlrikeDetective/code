# Data Visualization Projects Design System

This document specifies the design guidelines, color palette, and typography to maintain visual consistency across all data visualization projects in this workspace.

---

## 🎨 Color Palette

The color theme is inspired by organic, earthy tones paired with deep, calming teals. The background for all visualizations and UI layouts is `#BED0D0`.

| Color | Hex Code | Usage | Preview |
| :--- | :--- | :--- | :--- |
| **Sage Background** | `#BED0D0` | Primary background color | <div style="background-color: #BED0D0; width: 60px; height: 20px; border: 1px solid #000;"></div> |
| **Rust / Terracotta** | `#6F452D` | Primary text, titles, dark accents | <div style="background-color: #6F452D; width: 60px; height: 20px; border: 1px solid #000;"></div> |
| **Warm Ochre / Sand** | `#B77651` | Secondary text, active states, warm highlights | <div style="background-color: #B77651; width: 60px; height: 20px; border: 1px solid #000;"></div> |
| **Deep Teal / Forest** | `#01393D` | Dark visualization marks, key headers, structural lines | <div style="background-color: #01393D; width: 60px; height: 20px; border: 1px solid #000;"></div> |
| **Soft Teal / Seafoam** | `#56989F` | Accent data points, gridlines, hover/interactive fills | <div style="background-color: #56989F; width: 60px; height: 20px; border: 1px solid #000;"></div> |

---

## font Typography

To establish an artsy yet highly readable editorial look, we pair an expressive display font with a classic, structured serif text font.

* **Header / Heading Text:**
  * **Font:** **Comba** (by Adobe Fonts)
  * **Style:** Artsy, bold, display-oriented layout. Used for main titles and section headers (`H1`, `H2`).
  * **CSS Fallback:** `'Comba', 'Cooper Black', 'Impact', sans-serif`
* **Body / UI / Visualization Labels:**
  * **Font:** **Bookmania** (by Adobe Fonts)
  * **Style:** Clean, readable, editorial serif. Used for body text, data labels, axes, legends, and general UI.
  * **CSS Fallback:** `'Bookmania', 'Georgia', 'Times New Roman', serif`

---

## 📊 Visualization Guidelines

1. **Background Integration:**
    * Ensure all charts explicitly set their background color to `#BED0D0` (or transparent if overlaid on a `#BED0D0` page).
2. **Color Mapping:**
    * Use `#01393D` for primary data elements (e.g., bars, bubbles).
    * Use `#B77651` and `#56989F` for highlights and category distinctions.
    * Gridlines should be soft and thin, using `#56989F` at a low opacity (e.g., `0.2`).
3. **Typography in Charts:**
    * Titles should be styled with a display font matching `Comba`'s characteristics.
    * Axes, labels, and tick marks should use `Bookmania` (or serif fallbacks like `Georgia`) with color `#6F452D`.
