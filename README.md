# Automation-Lab-Maintenance
Scripts Python d'automatisation de maintenance et d'audit réseau.
# Automatisation & Audit - NumLab Maintenance
Par Dimitry CONTOUT

Ce dépôt rassemble des solutions python développées pour optimiser la maintenance technique et la surveillance des infrastructures réseau du NumLab.

## Projets inclus

### 1. Diagnostic de sécurité Rréseau (audit_infrastructure.py)
Outil de monitoring utilisant les bibliothèques "socket" et "ssl" pour vérifier l'état des services web.
* Fonctionnalité : Détection de l'exposition de ports non-standard (ex: Port 888).
* Sécurité : Audit de la validité des certificats SSL (détection d'expiration).

### 2. Automatisation de Maintenance ("trieur.py")
Script de gestion de flux pour les postes de travail.
 Organisation : Tri automatique des fichiers par extension.
 Traçabilité : Génération d'un rapport d'audit "rapport_activite.txt" pour chaque session de maintenance.

Projets réalisés dans le cadre d'une candidature pour le renfort technique du NumLab
