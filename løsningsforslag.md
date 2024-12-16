Selvfølgelig! Her er et opdateret forslag, der inkluderer en beslutning om at vælge en **Private Cloud-løsning** i stedet for Public Cloud eller Hybrid Cloud, og hvordan det vil fungere i forhold til virksomhedens behov.

---

# **Løsningsforslag for T&T IT Infrastruktur: Private Cloud Løsning**

Dette løsningsforslag beskriver en **Private Cloud**-løsning for T&T, der integrerer alle nødvendige systemer, backup og administration. Dette valg er baseret på behovet for højere kontrol, sikkerhed og isolering, samt at det lever op til virksomhedens specifikke krav.

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

## **2. Private Cloud Løsning**

I stedet for at vælge en **Public Cloud** eller **Hybrid Cloud** løsning, vil T&T vælge en **Private Cloud-løsning**, som giver højere kontrol over data, bedre sikkerhed og bedre overholdelse af virksomhedens krav.

### **Valg af Private Cloud-løsning:**
- **Fordele ved Private Cloud**:
    - **Kontrol**: Full kontrol over alle data, systemer og infrastruktur.
    - **Sikkerhed**: Bedre sikkerhed, da dataene er hostet internt eller i et privat datacenter, hvilket reducerer risikoen for eksponering.
    - **Compliance**: Det er lettere at opfylde specifikke compliance-krav (f.eks. GDPR), når data ikke er gemt på eksterne offentlige cloudtjenester.
    - **Tilpasning**: En private cloud-løsning kan tilpasses virksomhedens specifikke behov og krav.
  
### **Private Cloud Arkitektur**
- Brug af **On-Premise Private Cloud** ved hjælp af værktøjer som **VMware vSphere** eller **OpenStack** til at administrere ressourcer, hvor al hardware og software er dedikeret til virksomheden.
- **Backup** håndteres både lokalt via **TrueNAS** og gennem en offsite backup-løsning i en **Private Cloud**.

---

## **3. Operativsystemer**

T&T vil fortsat anvende en kombination af **Windows** og **Linux** operativsystemer i deres private cloud-miljø for at understøtte forskellige systemkrav.

- **Linux**:
    - **Domain Controller**: Samba AD til Windows administration.
    - DNS, DHCP, MariaDB, File Server (FTP/Samba), Web Server, Mail Server og NextCloud server.
- **Windows**:
    - **Tekniker-PC**: Adgang til administrative værktøjer.
    - **Bruger-PC**: Adgang til internettet, fildeling og NextCloud klient.

---

## **4. Backup Strategi**

Backup forbliver baseret på **3-2-1 princippet**, men med fokus på den private cloud-løsning:
- **3 kopier af data**:
    - Live-data (på filserver, web-server og database).
    - Lokal backup til **TrueNAS**.
    - Offsite backup til **Private Cloud Backup**.
- **2 forskellige medier**:
    - NAS og cloud.
- **1 kopi offsite**:
    - I cloudmiljøet (privat cloud).

Dette sikrer, at T&T har en effektiv backup-struktur, der både beskytter mod lokale hardwarefejl og ekstern nedetid.

---

## **5. Domain Controller med Samba AD**

En **Private Cloud**-løsning giver mulighed for at centralisere bruger- og adgangsstyring:
- **Samba AD** opsættes som **Domain Controller** for at styre Windows-klienter.
- Brugere og grupper administreres centralt, og **Windows-klienter** tilsluttes domænet for central styring af:
    - Rettigheder.
    - Netværksadgang.
    - Fildeling via Samba.

---

## **6. Database og SQL Krav**

**MariaDB** vil håndtere kundeoplysninger og intranet data i den private cloud:
- **Database**: MariaDB vil blive hostet på lokale servere, og adgangen til databasen vil blive kontrolleret via private netværk.
  
### **Eksempler på SQL-syntax**:
#### Stored Procedure


#### JOIN Statement


## **7. Migration fra Private Cloud til Public Cloud**

Selvom T&T vælger at anvende en **Private Cloud-løsning**, bør de stadig overveje muligheden for at migrere til en **Public Cloud** i fremtiden for visse workloads, såsom backup eller redundans. Her er trinnene for migration:

1. **Analyse**: Vurdering af databaser og filstruktur i private cloud.
2. **Backup & Test**: Før migrering, lav test-backup og planlæg for overgang til en offentlig cloud-backupløsning.
3. **Data-overflytning**: Brug værktøjer som **rsync** eller private cloud migration services.
4. **Optimering**: Konfigurér de private cloud-ressourcer som **AWS S3**, **Azure SQL** eller lignende, hvis virksomheden vælger en offentlig cloud til fremtidig redundans eller specielle formål.

---

## **8. Sikkerhed**

I en **Private Cloud-løsning** vil T&T have fuld kontrol over sikkerheden:
- **PFSense Firewall** vil beskytte mod uautoriseret adgang både eksternt og internt.
- **Wazuh** implementeres som SIEM-løsning for at overvåge og håndtere logfiler og trusler.
- **Backup**: Offsite backup til en **Private Cloud Backup-løsning** sikrer beskyttelse mod datatab.
  
Sikkerhedsprotokoller såsom **VPN**, **TLS/SSL** kryptering og **Multi-Factor Authentication (MFA)** kan også implementeres for ekstra beskyttelse.

---

## **9. Dokumentation**

- **Topologidiagram** (detaljeret overblik over den private cloud-infrastruktur).
- **Database-ER diagram** (MariaDB struktur).
- **Klasse diagrammer** til systemintegration og dataflyd.
- Dokumentation af **Domain Controller opsætning** og Windows-klient integration.

---

## **Konklusion**

Ved at vælge en **Private Cloud-løsning** får T&T maksimal kontrol og sikkerhed over deres infrastruktur, samtidig med at de kan opfylde compliance-krav og sikre følsomme data. Dette forslag fokuserer på at optimere både eksisterende hardware og software i en privat cloud, der kan håndtere virksomhedens nuværende og fremtidige behov.

T&T kan fortsat drage fordel af cloud-baserede løsninger til backup og eventuel fremtidig skalerbarhed, men vil primært have kontrollen over data og applikationer i et privat miljø.