# Emergency-Department-CRUD-API
A Python-based CRUD API for real-time management of Emergency Department patient records. Developed as part of my Health Informatics academic thesis

## Overview
This repository contains a Python/Flask-based CRUD API designed for the real-time management of Emergency Department (ED) triage data. Developed as the core backend implementation of my Health Informatics academic thesis, this project supports a mobile application built to digitize the traditional paper-based nursing history form taken at the ED.

## Clinical Context & Value
In emergency clinical settings, data velocity and accuracy are critical. This API provides the foundational backend infrastructure to:
* Process patient demographics, medical history, and clinical triage data seamlessly.
* Enable real-time updates of patient status directly from a mobile device.
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
* Language & Framework: Python 3.x, Flask
* Database: MySQL (Hosted locally via XAMPP for development and testing)
* Frontend: MIT App Inventor
* Core Domains: Health Information Systems, API Development, Nursing Informatics, Clinical Data Structuring

## System Demonstration & UI
A system demonstration from the original thesis presentation is available below to show the real-time data flow between the mobile frontend and backend API:
* **Live Video Demo:** https://youtu.be/_Ihjtn92Z4I?si=aNHl42MnXNnJyGtj

### Application Interface
The `UI_screenshots` directory contains the visual documentation of the frontend mobile application, developed specifically for triage nurses using the drag-and-drop visual programming environment of **MIT App Inventor**.
