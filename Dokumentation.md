# T&T Cloud Løsning - Teknisk Dokumentation
[Logo/Billede]

## Projektinformation
**Projektperiode:** [16-12-24] - [10-1-25]  
**Deltagere:**  
- [Robin] ([robi2069@zbc.dk])
- [Navn] ([Email])

## Indholdsfortegnelse
[Automatisk genereret]

## 1. Arbejdsfordeling
| Opgave | Ansvarlig | Status |
|--------|-----------|---------|
| Infrastruktur design | | |
| NextCloud implementation | | |
| Firewall opsætning | | |
| Backup løsning | | |
| Dokumentation | | |

## 2. Problemformulering

### 2.1 Kundens Udfordringer
- Nuværende IT-infrastruktur er utilstrækkelig
- Manglende skalerbarhed
- Behov for forbedret datasikkerhed
- Ineffektiv filhåndtering

### 2.2 Ønskede Forbedringer
- Centraliseret filhåndtering
- Høj tilgængelighed
- Skalerbar løsning
- Robust backup-strategi

## 3. Opgavebeskrivelse
[Detaljeret beskrivelse af kundens opgave baseret på kravspecifikationen]

## 4. Løsningsforslag

### 4.1 Overordnet Arkitektur
[Indsæt netværksdiagram]

### 4.2 Komponenter
- Proxmox VE Cluster
- NextCloud Platform
- Backup Infrastructure
- Network Security

### 4.3 Afgrænsning
[Liste over elementer der ikke er omfattet af projektet]
### 4.4 Løsningsplan for Migration fra Private Cloud til Public Cloud
1. Forberedelse og Analyse
Før migrationen er det vigtigt at foretage en grundig analyse af den eksisterende private cloud-infrastruktur, herunder:

Vurdering af eksisterende systemer: Identifikation af alle de systemer, der skal flyttes til Azure, herunder:
Webserver (Next.js)
Mailserver (Postfix)
Database (MariaDB)
Backup og datalagring
Databeskyttelse: Vurdering af eventuelle juridiske og compliance-krav (f.eks. GDPR) og hvordan disse opfyldes i Azure.
Tjenesteafhængigheder: Identifikation af systemer, som er afhængige af hinanden, og hvordan migrationen skal udføres for at minimere nedetid.
2. Valg af Azure Tjenester og Infrastruktur
Vi vælger relevante Azure-tjenester baseret på behovet for performance, sikkerhed og skalerbarhed.

2.1 Webserver (Next.js)
Tjenestevalg: Azure App Service eller Azure Virtual Machines.
Azure App Service: Anbefales for en mere administreret løsning, der tilbyder automatiseret scaling, let deployment og integration med CI/CD pipelines.
Azure Virtual Machines: Anbefales, hvis vi har brug for mere kontrol over serverkonfigurationen.
2.2 Mailserver (Postfix)
Tjenestevalg: Azure Virtual Machines (VMs) til at hoste Postfix.
Postfix vil blive installeret og administreret på en Azure VM.
Alternativt kan vi overveje at bruge Microsoft 365 for en mere administreret e-mail-løsning.
2.3 Database (MariaDB)
Tjenestevalg: Azure Database for MariaDB.
Denne tjeneste tilbyder en fuldt administreret database med indbyggede funktioner som automatisk skalering, sikkerhed, backup og opdateringer.
2.4 Backup
Tjenestevalg: Azure Backup.
Vi opretter en sikker backup-løsning til alle relevante data (Web, Mail, DB) ved hjælp af Azure Backup for at sikre, at vi følger 3-2-1 backup-princippet (3 kopier, 2 medier, 1 offsite).
2.5 Networking
Tjenestevalg: Azure Virtual Network, Azure VPN Gateway, og Azure Load Balancer.
Konfiguration af et Azure Virtual Network (VNet) for at forbinde alle ressourcer i et sikkert netværk.
Opsætning af VPN Gateway for sikre forbindelser mellem den private infrastruktur og Azure.
Azure Load Balancer kan anvendes til at fordele trafik på tværs af webserverne for høj tilgængelighed.
3. Migration Trin-for-Trin
Trin 1: Sikkerhed og Backup
Backup af eksisterende data fra private cloud til lokal storage og cloud-backup.
Kryptering af data under overførsel og i hvile ved hjælp af Azure Storage Encryption og SSL/TLS for webtrafik.
Oprettelse af Azure Key Vault til at opbevare og beskytte følsomme oplysninger som API-nøgler og adgangskoder.
Trin 2: Opsætning af Azure Infrastruktur
Oprettelse af nødvendige Azure ressourcer (App Service, Virtual Machines, Database for MariaDB, Backup).
Konfiguration af Azure Virtual Network og Network Security Groups (NSG) for at sikre netværkets sikkerhed.
Oprettelse af Azure Active Directory (AAD) for centraliseret bruger- og adgangsstyring.
Konfiguration af Azure Firewall for at beskytte mod uautoriseret adgang.
Trin 3: Migration af Systemer
Webserver (Next.js)
Opret en Azure App Service eller en Azure VM til hosting af Next.js-applikationen.
Konfigurer CI/CD pipelines ved hjælp af Azure DevOps eller GitHub Actions for nem deployment.
Test applikationen i Azure for at sikre, at den fungerer korrekt.
Mailserver (Postfix)
Opret en Azure VM til at hoste Postfix.
Konfigurer Postfix på VM’en og sørg for, at alle e-mail-indstillinger fungerer korrekt.
Test mailserveren for korrekt funktionalitet og integration.
Database (MariaDB)
Opret en instans af Azure Database for MariaDB.
Migrer data fra den eksisterende MariaDB-server i private cloud til Azure MariaDB instansen.
Test forbindelsen til databasen og sørg for, at applikationerne fungerer korrekt med den nye database.
Backup
Opsæt Azure Backup til at tage backups af alle relevante systemer.
Test, at backupene fungerer korrekt og kan gendannes ved behov.
4. Sikkerhed og Compliance
Azure Active Directory (AAD) bruges til at håndtere brugere og rettigheder centralt.
Azure Security Center implementeres for at overvåge sikkerhed og risici.
Alle data krypteres både under overførsel og i hvile.
Azure Sentinel kan bruges til at overvåge sikkerhedslogfiler og detektere potentielle trusler.
5. Test og Optimering
Efter migrationen udfører vi omfattende tests:

Systemtest: Verificering af, at alle systemer fungerer korrekt efter migrationen (Next.js-applikation, Postfix-mailserver, MariaDB).
Ydeevnetest: Test af webserverens skalerbarhed ved at simulere trafik og sikre, at auto-scaling og load balancing fungerer korrekt.
Sikkerhedstest: Verificering af, at firewall-regler, netværksbeskyttelse og adgangskontroller er korrekt konfigureret.
Backup-test: Test af backup- og restore-processen for at sikre, at data kan gendannes korrekt.
6. Overvågning og Drift
Efter migreringen opsætter vi løbende overvågning og driftsstyring:

Azure Monitor til at overvåge ydeevne og status på applikationer og ressourcer.
Azure Log Analytics for at få indsigt i logdata og identificere eventuelle problemer.
Azure Cost Management til at holde styr på omkostninger og optimere ressourceforbruget.
7. Langsigtet Plan
Skalering: Efter migrationen vil vi fortsat kunne skalere ressourcerne baseret på behov ved hjælp af auto-scaling og Azure Load Balancer.
Automatisering: Vi kan implementere Azure Automation til at automatisere gentagne administrative opgaver.
Udvidelse af tjenester: Efterhånden som T&T’s behov udvikler sig, kan vi udvide med yderligere Azure-tjenester som Azure Kubernetes Service (AKS), Azure AI og Azure Machine Learning.
Opsummering
Denne plan sikrer en effektiv migration fra T&T’s private cloud til Microsoft Azure, og dækker alle aspekter fra forberedelse, opsætning af Azure-tjenester, migration af systemer, sikkerhed, test, og driftsstyring. Ved at vælge Azure App Service, Azure Virtual Machines, Azure Database for MariaDB og Azure Backup, får vi en skalerbar, sikker og pålidelig løsning for fremtidig drift.

Efter migrationen vil T&T have en fleksibel, cloud-baseret infrastruktur, der er klar til at imødekomme både nuværende og fremtidige krav.

## 5. Design og Systembeskrivelse

### 5.1 Hardware Specifikationer
[Detaljer fra kravspecifikationen]

### 5.2 Software Komponenter
[Liste over anvendt software]

### 5.3 Netværksdesign
[VLAN struktur og netværkstopologi]



## 6. Teoretisk Grundlag

### 6.1 Cloud Computing Koncepter

### 6.2 High Availability Principper

### 6.3 Backup Strategier

### 6.4 Svar på spørgsmål
1. Hvad er forskellen på Cloud Computing og Cloud Netværk?  
Cloud Computing handler om levering af computerressourcer som servere, storage, databaser og applikationer via internettet. Det muliggør fleksibel, skalerbar og on-demand adgang til IT-tjenester uden behov for fysisk hardware.  
Cloud Netværk fokuserer på netværksinfrastrukturen, der muliggør forbindelsen mellem forskellige cloud-tjenester og brugere. Det inkluderer virtuelle netværk, routing, firewalls og load balancers, som sikrer hurtig og sikker datatrafik.

2. Hvad er SAAS, PAAS, IAAS?  
Disse er de tre vigtigste cloud-servicekategorier:  
SaaS (Software as a Service) leverer software via internettet. Brugerne tilgår applikationer uden at skulle installere eller vedligeholde dem. Eksempler: Gmail, Dropbox, Slack.  
PaaS (Platform as a Service) tilbyder en platform til udvikling, test og udrulning af applikationer uden at bekymre sig om infrastrukturen. Eksempler: Heroku, Google App Engine.  
IaaS (Infrastructure as a Service) leverer virtuelle maskiner, storage og netværksressourcer. Brugerne administrerer operativsystemer og applikationer. Eksempler: AWS EC2, Microsoft Azure VM.

3. Hvad er forskellen på en privat cloud og public cloud?  
Privat cloud er en dedikeret infrastruktur til én organisation, enten on-premises eller hostet eksternt. Fordele: mere sikkerhed, kontrol og tilpassede løsninger. Ulemper: dyrere at vedligeholde og mindre skalerbar.  
Public cloud deles mellem flere kunder via en udbyder som AWS, Azure eller Google Cloud. Fordele: skalerbart, omkostningseffektivt og nemt at bruge. Ulemper: begrænset kontrol og mulige sikkerhedsproblemer.

4. Hvad er Ubuntu Cloud?  
Ubuntu Cloud refererer til en cloud-platform baseret på Ubuntu Linux-operativsystemet. Canonical, firmaet bag Ubuntu, tilbyder:  
Ubuntu OpenStack, en version af OpenStack optimeret til Ubuntu; Charmed OpenStack, et værktøj til nem implementering af private clouds; og Ubuntu Advantage, support til cloud-miljøer. Det er populært i private og hybrid-clouds på grund af sin stabilitet og open-source natur.

5. Hvad er OpenStack?  
OpenStack er en open-source platform til cloud computing, der lader brugere opbygge og administrere private eller offentlige clouds. Det består af flere moduler, fx Nova (compute), Swift (storage), Neutron (networking). OpenStack er velegnet til virksomheder, der ønsker en fleksibel og skræddersyet cloud-infrastruktur.

6. Hvad er VMware vSphere?  
VMware vSphere er en virtualiseringsplatform, der giver virksomheder mulighed for at køre virtuelle maskiner og administrere datacentre effektivt. Den inkluderer vCenter Server til centraliseret administration og ESXi til virtualisering af hardware. Bruges ofte i private clouds og hybrid-clouds.

7. Hvad er Kubernetes og hvad kan det bruges til?  
Kubernetes (k8s) er en open-source platform til orkestrering af containeriserede applikationer. Den automatiserer udrulning, skalering og administration af containere og gør det nemt at håndtere komplekse applikationer fordelt over flere servere. Bruges til at køre moderne applikationer i både cloud og on-premises miljøer.

8. Hvad er forskellen på Google Cloud vs AWS vs Azure?  
Google Cloud Platform (GCP) er stærk inden for dataanalyse og maskinlæring (BigQuery, TensorFlow) og har fokus på open-source integrationer.  
Amazon Web Services (AWS) er markedets førende udbyder med det bredeste udvalg af tjenester og er velegnet til store virksomheder og fleksible miljøer.  
Microsoft Azure integrerer problemfrit med Windows og Office-produkter og er populær blandt virksomheder med eksisterende Microsoft-infrastruktur.

9. Hvad er forskellen på Cloud Clustering og Cloud Computing?  
Cloud Clustering handler om at forbinde flere servere (noder) i et cluster for at forbedre ydelse og redundans. Det anvendes til applikationer, der kræver høj tilgængelighed og failover-mekanismer.  
Cloud Computing er en bredere betegnelse for levering af computerressourcer via internettet med fokus på fleksibilitet, skalerbarhed og reduceret infrastrukturstyring. Cloud Clustering er ofte en underkategori af Cloud Computing, der specifikt forbedrer driftssikkerhed.

## 7. Implementation
[Henvisning til teknisk vejledning]


### 8.1 Sikkerhedsforanstaltninger

### 8.2 Adgangsstyring

### 8.3 Backup og Recovery


## 9. Diskussion

### 9.1 Udfordringer

### 9.2 Løsninger

### 9.3 Fremtidige Forbedringer

## 10. Konklusion

## 11. Referencer og Bilag

### 11.1 Kilder

### 11.2 Eksterne Referencer

### 11.3 Bilag

## 12. Daglig Logbog
| Dato | Aktiviteter | Udfordringer | Løsninger |
|------|-------------|--------------|-----------|
| | | | |
