# Emergency-Department-CRUD-API
A Python-based CRUD API for real-time management of Emergency Department patient records. Developed as part of my Health Informatics academic thesis

## Overview
This repository contains a Python-based CRUD API designed for the real-time management of Emergency Department (ED) patient records. Developed as the core technical implementation of my Health Informatics academic thesis, this project digitizes traditional paper-based nursing forms into a structured, easily accessible Electronic Health Record (EHR) module.

## Clinical Context & Value
In emergency clinical settings, data velocity and accuracy are critical. This API provides the foundational backend infrastructure to:
* Process patient demographics and clinical triage data seamlessly.
* Enable real-time updates of patient status.
* Ensure data integrity and structural validity prior to database ingestion, supporting evidence-based clinical decision-making at the point of care.

## Repository Structure
The system follows a modular architecture, separating the core CRUD operations to ensure maintainability and scalability:

* api.py : The central routing module that orchestrates API requests and endpoints.
* create.py : Handles the secure ingestion and structuring of new ED admissions and triage data.
* read.py : Manages fast data retrieval, enabling real-time querying for healthcare professionals.
* update.py : Processes continuous clinical modifications ensuring data consistency.
* delete.py : Executes the safe deletion or archiving of patient records in compliance with system rules.
* db.py: Establishes the connection to the MySQL database (credentials replaced with placeholders for security).

## Security & Data Privacy Statement
**Strictly No PHI/PII:** Operating within the rigorous frameworks of Health Informatics and Data Governance, privacy is paramount. 
* This repository contains **only structural code and functional logic**. 
* Any data utilized within these scripts for testing purposes are 100% synthetic, dummy data (e.g., "John Doe") used exclusively for demonstration. 
* No real Protected Health Information (PHI) or Personally Identifiable Information (PII) is included, and database connection credentials have been intentionally omitted to adhere to security best practices.

## Tech Stack & Domain
* **Language:** Python 3.x
* **Core Domains:** Health Information Systems, API Development, Clinical Data Structuring
