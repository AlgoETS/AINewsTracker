"use client"

import { Container, Grid } from "@mantine/core";
import ArticleCard from "./ArticleCard";

const Dashboard = ({ articles }) => (
  <Container size="lg">
    <Grid gutter="md">
      {articles.map((article) => (
        <ArticleCard key={article.id} article={article} />
      ))}
    </Grid>
  </Container>
);

export default Dashboard;
