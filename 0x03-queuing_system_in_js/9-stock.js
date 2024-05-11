import express from 'express';
import Redis from 'redis';

const app = express();
const client = Redis.createClient();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

const getItemById = (id) => {
  return listProducts.find((item) => (link unavailable) === id);
};

app.get('/list_products', (req, res) => {
  const products = listProducts.map((item) => ({
    itemId: (link unavailable),
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: (link unavailable),
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

const reserveStockById = async (itemId, stock) => {
  await client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await client.get(`item.${itemId}`);
  return parseInt(stock) || 0;
};

app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

