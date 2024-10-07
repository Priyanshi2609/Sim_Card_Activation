"SIM Card Activation"
This project implements a SIM Card Activation service for a telecom company using FastAPI and MongoDB. The service includes APIs to activate/deactivate SIM cards, fetch SIM card details, and handle error scenarios.
Features:
-Activate SIM Card: Activate a SIM card and record its activation date.
-Deactivate SIM Card: Deactivate a SIM card.
-Get SIM Details: Retrieve details about a SIM card, including its number, phone number, status, and activation date.
-Error Handling: Gracefully handle scenarios such as SIM card not found, invalid state transitions (e.g., activating an already active SIM), and missing/invalid input.
Technologies Used:
-Python: Primary programming language.
-FastAPI: Web framework for building APIs.
-MongoDB: NoSQL database for storing SIM card information.
-Pydantic: Data validation and parsing.
-Uvicorn: ASGI server to run FastAPI applications.
