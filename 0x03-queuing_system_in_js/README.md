# Project: 0x03. Queuing System in JS

![Redis Server](./redis_server.png)

## Resources

### Read or watch:-

- [Redis quick start](https://redis.io/docs/latest/integrate/)
- [Redis client interface](https://redis.io/docs/latest/develop/connect/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue](https://github.com/Automattic/kue) *deprecated but still use in the industry*

### and…

Don’t forget to run `$ npm install` when you have the `package.json`

## Installation and Setup

1. Download and extract Redis:

```bash
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
```

## Tasks

### 0. [Install a redis instance] | [README.md](./README.md), [dump.rdb](./dump.rdb) :-

Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/downloads/](https://redis.io/downloads/)):

```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
```

- Start Redis in the background with `src/redis-server`

```bash
src/redis-server &
```

- Make sure that the server is working with a ping `src/redis-cli ping`

```bash
PONG
```

- Using the Redis client again, set the value `School` for the key `Holberton`

```bash
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

- Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)

```bash
kill [PID_OF_Redis_Server]
```

- Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Requirements:

- Running `get Holberton` in the client, should return `School`

| Task | File |
| ---- | ---- |
| 1. Node Redis Client | [0-redis_client.js](./0-redis_client.js) |
| 2. Node Redis client and basic operations | [1-redis_op.js](./1-redis_op.js) |
| 3. Node Redis client and async operations | [2-redis_op_async.js](./2-redis_op_async.js) |
| 4. Node Redis client and advanced operations | [4-redis_advanced_op.js](./4-redis_advanced_op.js) |
| 5. Node Redis client publisher and subscriber | [5-subscriber.js](./5-subscriber.js), [5-publisher.js](./5-publisher.js) |
| 6. Create the Job creator | [6-job_creator.js](./6-job_creator.js) |
| 7. Create the Job processor | [6-job_processor.js](./6-job_processor.js) |
| 8. Track progress and errors with Kue: Create the Job creator | [7-job_creator.js](./7-job_creator.js) |
| 9. Track progress and errors with Kue: Create the Job processor | [7-job_processor.js](./7-job_processor.js) |
| 10. Writing the job creation function | [8-job.js](./8-job.js) |
| 11. Writing the test for job creation | [8-job.test.js](./8-job.test.js) |
| 12. In stock? | [9-stock.js](./9-stock.js) |
