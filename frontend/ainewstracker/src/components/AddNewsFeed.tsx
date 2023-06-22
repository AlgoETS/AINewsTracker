import React from 'react';

const AddNewsFeed = () => {
    return (
        <div>
            <h1>Configure News Feed</h1>
            <form>
                <label>
                    Link:
                    <input type="text" name="link" />
                </label>
                <label>
                    Number of articles:
                    <input type="number" name="number_of_articles" />
                </label>
                <label>
                    Sector:
                    <input type="text" name="sector" />
                </label>
                <label>
                    Country:
                    <input type="text" name="country" />
                </label>
                <label>
                    Language:
                    <input type="text" name="language" />
                </label>
                <label>
                    Type:
                    <input type="text" name="type" />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
}

export default AddNewsFeed;
