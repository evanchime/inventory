# Inventory Python Project

This is a Python project for managing inventory. It allows users to keep track of shoes, their quantities, and other relevant information.

## Installation (Running Directly on Your Localhost)

1. Clone the repository: `git clone https://github.com/evanchime/inventory.git`
2. Navigate to the project directory: `cd inventory`
3. Create a virtual enviroment: `python3 -m venv venv` 
   - On Unix-based systems (Linux/macOS): `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Running Directly on Your Localhost
   - Run the main script: `python3 inventory.py your_inventory_file`
   - Follow the on-screen instructions to interact with the inventory system.

2. Running on Docker Container
   - On Unix-based systems (Linux/macOS. Ensure you've root priviledges): `docker run -i -v path_to_your_inventory_file:/data evanchime/inventory-app /data/your_inventory_file`
   - On Windows (Ensure you've admin privileges): `docker run -i -v path_to_your_inventory_file:/data evanchime/inventory-app /data/your_inventory_file`
   - Follow the on-screen instructions to interact with the inventory system.

Don't forget to replace path_to_your_inventory_file and your_inventory_file accordingly

## Features

- Add new shoes to the inventory
- Update shoe quantities
- View all shoes in the inventory
- Determine the product with the lowest quantity and restock it.
- Search products by code.
- Calculate the total value for each shoe
- Show shoes on sale

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -am 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.
