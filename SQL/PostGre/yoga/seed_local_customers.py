import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer

def seed_customers():
    """
    Seeds the database with local customers from Tarifa, Spain.
    """
    customers_data = [
        (175,"Claudia","Velasco Ortiz","claudia.velasco.o@enlace.es","2026-03-08 11:01:45.152239"),
        (174,"Samuel","Torres Galdós","s.torres.g@construye.es","2026-03-08 11:01:14.73627"),
        (173,"Natalia","Salazar Mora","n.salazar.mora@vanguardia.es","2026-03-08 11:00:54.00541"),
        (172,"Fernando","Ríos Vargas","f.rios.vargas@ciencias.es","2026-03-08 11:00:19.502115"),
        (171,"Isabel","Quintana Rojas","i.quintana.r@estilo.es","2026-03-08 10:59:46.229776"),
        (170,"Nicolás","Paredes Méndez","n.paredes.m@red.es","2026-03-08 10:58:47.950621"),
        (169,"Beatriz","Olivares Guerra","b.olivares.g@comunicaciones.es","2026-03-08 10:57:19.289225"),
        (168,"Diego","Navarro Duque","diego.navarro.d@empresa.es","2026-03-08 10:56:31.484701"),
        (167,"Camila","Montoya Serrano","c.montoya.s@academia.es","2026-03-08 10:54:09.835121"),
        (166,"Hugo","Lozano Castillo","h.lozano.c@webmail.es","2026-03-08 10:53:29.88208"),
        (165,"Valeria","Jiménez Bravo","v.jimenez.bravo@diseno.es","2026-03-08 10:52:34.877831"),
        (164,"Sebastián","Ibarra Flores","sibarra.flores@consultoria.es","2026-03-08 10:51:19.345618"),
        (163,"Sofía","Heredia Nazario","s.heredia.n@nube.es","2026-03-08 10:50:08.909081"),
        (162,"Adrián","Gallego Santos","adrian.gallego.s@servicios.es","2026-03-08 10:48:38.17962"),
        (161,"Martina","Ferrer Blanco","martina.ferrer.b@global.com","2026-03-08 10:48:00.843837"),
        (160,"Rodrigo","Escudero Peña","r.escudero.p@proyectos.es","2026-03-08 10:46:56.982686"),
        (159,"Elena","De la Cruz Montes","elena.delacruz.m@estudio.es","2026-03-08 10:45:26.014548"),
        (158,"Mateo","Castañeda Vidal","m.castaneda.vidal@red.es","2026-03-08 10:44:30.471195"),
        (157,"Lucía","Beltrán Orozco","lucia.beltran.o@correo.es","2026-03-08 10:43:22.431161"),
        (156,"Javier","Alarcón Ruiz","j.alarcon.ruiz@ficticia.es","2026-03-08 10:42:46.701391"),
    ]

    customers_to_create = []
    for cid, fname, lname, email, jdate in customers_data:
        full_name = f"{fname} {lname}"
        
        # Check if customer already exists to avoid UniqueConstraint violations
        if not Customer.objects.filter(email=email).exists():
            customer = Customer(
                id=cid,
                name=full_name,
                email=email,
                city="Tarifa",
                country="Spain",
                customer_type="LOCAL",
                created_at=jdate
            )
            customers_to_create.append(customer)
    
    if customers_to_create:
        # bulk_create is used to efficiently insert multiple records.
        # Note: on some databases, auto_now_add=True might still override created_at
        # unless handled specifically, but it's the most idiomatic way for bulk operations.
        Customer.objects.bulk_create(customers_to_create)
        print(f"Successfully added {len(customers_to_create)} customers.")
    else:
        print("No new customers to add.")

if __name__ == "__main__":
    seed_customers()
