import React, { useEffect, useState } from 'react';

const NewsFeeds = () => {
    const [feeds, setFeeds] = useState([]);

    // Replace this function with actual data fetching
    const fetchFeeds = async () => {
        const dummyData = [
            {id: '1', link: 'https://example.com', number_of_articles: 10, sector: 'Tech', country: 'USA', language: 'English', type: 'Web'},
            {id: '2', link: 'https://example2.com', number_of_articles: 5, sector: 'Finance', country: 'UK', language: 'English', type: 'Web'},
        ];

        setFeeds(dummyData);
    };

    useEffect(() => {
        fetchFeeds();
    }, []);

    return (
        <div>
            <h1>News Feeds</h1>
            {feeds.map(feed => (
                <div key={feed.id}>
                    <h2>{feed.link}</h2>
                    <p>Number of articles: {feed.number_of_articles}</p>
                    <p>Sector: {feed.sector}</p>
                    <p>Country: {feed.country}</p>
                    <p>Language: {feed.language}</p>
                    <p>Type: {feed.type}</p>
                </div>
            ))}
        </div>
    );
}

export default NewsFeeds;
