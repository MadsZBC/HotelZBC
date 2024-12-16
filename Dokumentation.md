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
