import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Company = () => {
    const [companies, setCompanies] = useState([]);

    useEffect(() => {
        const fetchCompanies = async () => {
            const result = await axios('/api/companies'); // replace with your actual API endpoint
            setCompanies(result.data);
        };

        fetchCompanies();
    }, []);

    return (
        <div>
            <h1>All Companies</h1>
            {companies.map(company => (
                <div key={company.id}>
                    <h2>{company.name}</h2>
                    <p>{company.description}</p>
                    {/* Add more company details as needed */}
                </div>
            ))}
        </div>
    );
};

export default Company;
