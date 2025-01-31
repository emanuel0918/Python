import os
import json
import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

routes = web.RouteTableDef()

VERIFY_TOKEN = os.getenv('VERIFY_TOKEN', 'defaultVerifyToken')

@routes.get("/income")
async def verify_webhook(request):
    mode = request.query.get("hub.mode")
    token = request.query.get("hub.verify_token")
    challenge = request.query.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        # If it matches, respond with hub.challenge
        return web.Response(text=challenge)
    else:
        return web.json_response({"error": "Verification failed"}, status=403)


@routes.post('/income')
async def receive_webhook(request):
    body = await request.json()
    logger.info(f"Received body: {json.dumps(body, indent=2)}")
    # Process the webhook...
    return web.json_response({"status": "EVENT_RECEIVED"}, status=200)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=3979)
