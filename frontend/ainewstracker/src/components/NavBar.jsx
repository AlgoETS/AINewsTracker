"use client";
import { Flex, Container, Paper, Button } from '@mantine/core';
import Link from 'next/link';
import Image from 'next/image';

const NavBar = () => (
    <Paper padding="md" shadow="xs">
        <Container>
            <Flex justify="between" align="center">
                <Image
                    src="/AINewsTracker_transparent.svg"
                    alt="Logo"
                    width={100}
                    height={24}
                />
                <Flex>
                    <Link href="/SignIn" passHref>
                        <Button variant="outline" color="blue" className="mr-4">Sign In</Button>
                    </Link>
                    <Link href="/SignUp" passHref>
                        <Button color="blue">Sign Up</Button>
                    </Link>
                </Flex>
            </Flex>
        </Container>
    </Paper>
);

export default NavBar;
