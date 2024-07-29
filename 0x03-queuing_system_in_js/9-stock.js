const express = require('express');
const app = express();
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

const getAsync = promisify(client.get).bind(client);

const listProducts = [
	{"itemId": 1, "itemName": "Suitcase 250", "price": 50, "initialAvailableQuantity": 4},
	{"itemId": 2, "itemName": "Suitcase 450", "price": 100, "initialAvailableQuantity": 0},
	{"itemId": 3, "itemName": "Suitcase 650", "price": 350, "initialAvailableQuantity": 2},
	{"itemId": 4, "itemName": "Suitcase 1050", "price": 550, "initialAvailableQuantity": 5}
];

function getItemById(id) {
	return listProducts.find(product => product.itemId == id);
}

app.get('/list_products', (req, res) => {
	res.send(listProducts);
});

function reserveStockById(itemId, stock) {
	client.set(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId) {
	const value = await getAsync(itemId);
	return value;
}

app.get('/list_products/:itemId', (req, res) => {
	const id = req.params.itemId;
	const product = getItemById(parseInt(id));
	if (product) {
		res.send(product);
	} else {
		res.send({"status":"Product not found"});
	}
});

app.get('/reserve_product/:itemId', (req, res) => {
	const id = req.params.itemId;
	const product = getItemById(parseInt(id));
	if (!product) {
		res.send({"status":"Product not found"});
	}
	else {
		if (product.initialAvailableQuantity < 1) {
			res.send({"status": "Not enough stock available", "itemId": `${parseInt(id)}`});
		}
		else {
			reserveStockById(id, product.toString());
			res.send({"status":"Reservation confirmed","itemId":`${parseInt(id)}`});
		}
	}
});

app.listen(1245);
