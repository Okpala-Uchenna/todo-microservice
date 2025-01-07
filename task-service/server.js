const express = require('express');
const redis = require('redis');
const app = express();
const port = 80;

const client = redis.createClient({
  host: 'redis',
  port: 6379
});

client.on('connect', function () {
  console.log('Connected to Redis');
});

app.get('/', (req, res) => {
  res.send('Task service is up and running!');
});

app.listen(port, () => {
  console.log(`Task service is listening at http://localhost:${port}`);
});
