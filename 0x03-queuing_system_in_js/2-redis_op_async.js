import { promisify } from 'util';
import { createClient } from 'redis';
const redis = require('redis');

const client = createClient();

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
	console.log('Redis client connected to the server');
});
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
	const reply = await setAsync(schoolName, value);
	redis.print(`Reply: ${reply}`);
}
async function displaySchoolValue(schoolName) {
	const value = await getAsync(schoolName);
	console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
