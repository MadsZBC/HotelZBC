Her er det opdaterede løsningsforslag med en **Domain Controller Server** (Linux-baseret) og specifikationer for **Windows-klienter** opdelt mellem teknikere og brugere:

---


# **Løsningsforslag for T&T IT Infrastruktur**

Dette løsningsforslag integrerer en **Private Cloud**-løsning med backup, et **mixet miljø af Windows og Linux** samt de angivne systemkrav.

---

## **1. Infrastruktur og Komponenter**

### **Topologisk Oversigt**
- **DMZ Zone**: Adskilt med **PFSense Firewall** for ekstern og intern netværksbeskyttelse.
    - **Web Server**: Intranet CMS (f.eks. WordPress, Joomla) koblet til MariaDB.
    - **Mail Server**: Postfix eller Mailu som mail-løsning.
- **Intern Zone**:
    - **Domain Controller (Linux)**: Administrerer Windows-klienter og brugere med f.eks. **Samba AD** (Active Directory kompatibilitet).
    - **DNS Server**: Lokal DNS-løsning til intern navneopløsning.
    - **DHCP Server**: Automatiseret IP-konfiguration.
    - **NextCloud Server**: Privat cloud til intern fildeling og mail-klient.
    - **MariaDB**: Database til kundeoplysninger og backend til intranet.
    - **File Server**: Fildeling via FTP og Samba i Linux-miljø.
    - **Wazuh**: SIEM (Security Information & Event Management) til overvågning.
- **Backup**:
    - **TrueNAS**: Bruges til backup-løsning af mail, filserver og database.
    - **Cloud Backup**: Sikring med 3-2-1 backup-princippet (3 kopier, 2 typer medier, 1 offsite cloud-kopi).
- **Windows Klienter**:
    - **Tekniker-PC**: En Windows-klient med administrative værktøjer.
    - **Bruger-PC**: En separat Windows-klient til brugernes daglige arbejde.

---

## **2. Cloud Løsning**
Efter en vurdering af virksomhedens behov og budget foreslås følgende:

- **Private Cloud**:
    - **NextCloud** fungerer som platform til intern fildeling og mail-klient.
    - Backup håndteres med **TrueNAS** og cloud-backup (f.eks. AWS S3, Google Cloud Storage eller Azure).
- **Public Cloud (fremtidig plan)**:
    - Mulighed for at migrere backup og databasesystemer til Public Cloud (f.eks. Amazon RDS, Azure SQL).

---

## **3. Operativsystemer**
- **Linux**:
    - **Domain Controller**: Samba AD til Windows administration.
    - DNS, DHCP, MariaDB, File Server (FTP/Samba), Web Server, Mail Server og NextCloud server.
- **Windows**:
    - **Tekniker-PC**: Adgang til administrative værktøjer.
    - **Bruger-PC**: Adgang til internettet, fildeling og NextCloud klient.

---

## **4. Backup Strategi**
Backup tager udgangspunkt i **3-2-1 princippet**:
- **3 kopier af data**:
    - Live-data (på filserver, web-server og database).
    - Lokal backup til **TrueNAS**.
    - Offsite backup til **Cloud Backup** (AWS S3/Google Cloud).
- **2 forskellige medier**:
    - NAS og cloud.
- **1 kopi offsite**:
    - I cloudmiljø.

---

## **5. Domain Controller med Samba AD**
- **Samba AD** opsættes som **Domain Controller** for at styre Windows-klienter.
- Brugere og grupper administreres centralt.
- **Windows-klienter** tilsluttes domænet for central styring af:
    - Rettigheder.
    - Netværksadgang.
    - Fildeling via Samba.

---

## **6. Database og SQL Krav**
**MariaDB** vil håndtere kundeoplysninger og intranet data. Eksempler på SQL-syntax:

### **Stored Procedure**
```sql
DELIMITER $$
CREATE PROCEDURE GetCustomerData(IN CustomerID INT)
BEGIN
    SELECT * FROM Customers WHERE ID = CustomerID;
END$$
DELIMITER ;
```

### **JOIN Statement**
```sql
SELECT Orders.OrderID, Customers.Name
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.ID;
```

---

## **7. Migration fra Private Cloud til Public Cloud**
1. **Analyse**: Vurdering af databaser og filstruktur.
2. **Backup & Test**: Før migrering, lav test-backup.
3. **Data-overflytning**: Brug værktøjer som **rsync** eller cloud migration services.
4. **Optimering**: Konfigurér cloud-services som AWS S3, RDS eller Azure SQL.

---

## **8. Sikkerhed**
- **PFSense Firewall** beskytter mod uautoriseret adgang.
- **Wazuh** implementeres til log-management og overvågning.
- **Domain Controller** styrer brugertilgange og sikkerhedsrettigheder.
- **Backup** sikrer datatab mod f.eks. ransomware-angreb.

---

## **9. Dokumentation**
- **Topologidiagram** (som dit nuværende).
- **Database-ER diagram** (MariaDB).
- **Klasse diagrammer** til systemintegration og dataflyd.
- Dokumentation af **Domain Controller opsætning** og Windows-klient integration.

---

Dette forslag sikrer en **robust, fleksibel og fremtidssikret løsning** for virksomheden T&T, med styring af både Linux og Windows miljøer.
