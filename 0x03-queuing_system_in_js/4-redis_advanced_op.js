import { createClient } from 'redis';
const redis = require('redis');

const client = createClient();

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.hset('HolbertonSchools', 'Portland', '50', (err, reply) => {
	redis.print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Seattle', '20', (err, reply) => {
        redis.print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'New York', '80', (err, reply) => {
        redis.print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Bogota', '20', (err, reply) => {
        redis.print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Cali', '40', (err, reply) => {
        redis.print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Paris', '2', (err, reply) => {
        redis.print(`Reply: ${reply}`);
});

client.hgetall('HolbertonSchools', (err, reply) => {
	console.log(reply);
});
