Description:

The OLX Scraper project is a FastAPI-based web application designed to scrape listing data from the OLX platform, save it into a PostgreSQL database, and automate periodic tasks such as database dumps and regular scraping. The application is containerized using Docker and includes task scheduling via APScheduler for efficient periodic operations.

Data Scraping:
1. Scrapes listing data from OLX (titles, descriptions, views, service types, and URLs).
Uses BeautifulSoup for HTML parsing and data extraction.
2. Database Integration:
Stores scraped data in a PostgreSQL database.
Utilizes SQLAlchemy for ORM functionality, enabling smooth CRUD operations.
3. Automation:
Automates periodic scraping using APScheduler.
Creates daily database dumps for backup.
4. Logging and Utility Functions:
Implements helper utilities for logging, data formatting, and directory management.
5. Containerization:
Dockerized for deployment using docker-compose.
Includes a wait-for-it.sh script to ensure PostgreSQL is ready before the application starts.
6. Scalability:
Modular design for ease of maintenance and scalability.
Can be extended to scrape other websites or add additional features.

Technologies Applied:
Backend Framework - FastAPI: A modern Python web framework for building APIs.
Web Scraping - BeautifulSoup: Library for extracting data from HTML and XML documents.
Requests - HTTP library for making requests to the OLX website.
Database - PostgreSQL: A relational database for storing scraped data. SQLAlchemy: Object Relational Mapper (ORM) for database interaction.
Task Scheduling - APScheduler: Python library for scheduling tasks such as periodic scraping and database dumps.
Containerization - Docker: Ensures the application can be deployed consistently across environments. Docker Compose: Manages multi-container application deployment.
Other Utilities - Shell scripting (wait-for-it.sh) for ensuring service readiness. Logging for tracking events and errors.
