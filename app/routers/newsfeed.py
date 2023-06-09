
@app.get("/rss_feeds/{feed_id}")
def get_rss_feed(feed_id: str):
    rss_feed = collections["rss_feeds"].find_one({"_id": feed_id})
    return {"rss_feed": rss_feed}
