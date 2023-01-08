# santa-voice

## Testing

Build and run docker services:
```
docker-compose build
docker-compose up
```
Listen for published messages:
```
mosquitto_sub -p 18883 -t '#' -v
```
Send test message:
```
mosquitto_pub -p 18883 -t santa -m test
```
