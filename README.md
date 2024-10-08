Microservices Project: User, Order, and Payment Management

This project is a microservice-based system built using FastAPI to manage users, orders, and payments. The architecture is designed to ensure scalability, flexibility, and maintainability, with each microservice having its own database, logic, and APIs. 
Each microservice functions independently and communicates through HTTP requests. The structure includes:

User Service: Responsible for managing user-related operations (registration, login, etc.). Provides user information to the Order Service during order creation.

Order Service: Manages orders and their status. It interacts with both the User Service to validate user details .

Payment Service: Manages the payment process, ensuring that an order exists before processing a transaction. It interacts with the Order Service to validate order data.


Service Communication

The services communicate through RESTful APIs using HTTP requests. For example:
    The Payment Service calls the Order Service to ensure the order exists before processing payments.

    async def get_order(order_id: int):
      async with httpx.AsyncClient() as client:
          response = await client.get(f"{ORDER_SERVICE_URL}/{order_id}")
              if response.status_code == 404:
                  return None
              return OrderAdapter.adapt(response.json())
        
If the order is found, the payment is processed. If not, a 404 error (order not found) is returned.        


Technology Stack

FastAPI: A modern, high-performance Python web framework used to build the APIs for each service. FastAPI provides automatic generation of API documentation (via Swagger and ReDoc) and supports asynchronous programming for improved request handling.

Pydantic: Used for data validation and serialization within the FastAPI models. Ensures strict validation of user input and clean data handling.

SQLAlchemy: As the ORM (Object Relational Mapping) tool, SQLAlchemy handles database operations and transactions for each service, supporting both synchronous and asynchronous operations.

PostgreSQL: Each microservice uses its own PostgreSQL database to store service-specific data. This ensures that the services are independent and can scale as needed.

HTTPX: For communication between microservices. For example, the Payment Service uses HTTPX to verify order details with the Order Service before processing a payment.

Alembic: Used for managing database migrations, ensuring that changes to the database schema are versioned and applied correctly across environments.

SOLID Design Principles: The codebase adheres to SOLID principles to maintain clean and maintainable code. Patterns like Factory, Strategy, and Facade have been used to implement modular, scalable solutions.


Steps to Run

Clone the repository:

    git clone https://github.com/yourusername/microservices-project.git

Each microservice will be available at its respective port. For example:

    User Service: http://localhost:8000
    Order Service: http://localhost:8001
    Payment Service: http://localhost:8002

This README gives a detailed overview of your microservices architecture, technologies used, and how to set up the project. You can tweak it based on specific project needs or future improvements.
