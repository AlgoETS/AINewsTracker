"use client"
import Image from 'next/image';
import Dashboard from '../components/Dashboard';
import NavBar from '../components/NavBar';
import articles from '../data/articles.json';
import { Container, Paper, Text, MantineProvider } from '@mantine/core';
import React from 'react';


export default function Home() {
    return (
        <MantineProvider
            withGlobalStyles
            withNormalizeCSS
            theme={{
                colorScheme: 'dark',
                colors: {
                    green: ['#d5f5e3', '#a3d9a5', '#68bd63', '#34a853', '#0b6623', '#004d00'],
                    purple: ['#f5d5fa', '#e8a3f0', '#da72e4', '#cb40d9', '#9c00af', '#670075'],
                },
                shadows: {
                    md: '1px 1px 3px rgba(0, 0, 0, .25)',
                    xl: '5px 5px 3px rgba(0, 0, 0, .25)',
                },
                headings: {
                    fontFamily: 'Roboto, sans-serif',
                    sizes: {
                        h1: { fontSize: '2rem' },
                    },
                },
            }}
            >
            <Container className="flex flex-col items-center justify-between mt-16">
                <Paper shadow="xs">
                    <Text align="center" size="xl" weight={500}>Welcome to AINewsTracker</Text>
                    <Text align="center">AINewsTracker is a sophisticated web application that backtests the influence of financial news on the stock market. It utilizes artificial intelligence to categorize, filter, and analyze financial news from a variety of trustworthy international and regional sources.</Text>
                </Paper>
                <Dashboard articles={articles} />
            </Container>
        </MantineProvider>
    );
}
