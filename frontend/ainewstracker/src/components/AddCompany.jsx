import React, { useState } from 'react';

const AddCompany = () => {
    const [company, setCompany] = useState({
        name: '',
        ticker: '',
        description: '',
        website: '',
        industry: '',
        sector: '',
        country: ''
    });

    const handleChange = e => {
        setCompany({ ...company, [e.target.name]: e.target.value });
    };

    const handleSubmit = e => {
        e.preventDefault();
        console.log(company);
        // Call your API to add company
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* Replace these with your actual form fields */}
            <input name="name" value={company.name} onChange={handleChange} placeholder="Name" />
            {/* More inputs for each field */}
            <button type="submit">Add Company</button>
        </form>
    );
};

export default AddCompany;
