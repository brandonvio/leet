docker build -t cc/price .
docker run -d -p 3000:3000 cc/price
# docker logs --follow f77035b64be6