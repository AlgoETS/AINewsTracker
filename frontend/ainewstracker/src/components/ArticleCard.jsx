import { Card, Text, Flex, Accordion, Badge, Button, Image } from '@mantine/core';
import Link from 'next/link';

const ArticleCard = ({ article }) => (
  <Card shadow="sm" padding="lg" radius="md" withBorder>
    <Card.Section>
      <Image
        src={article.imageUrl}
        height={160}
        alt="Article image"
      />
    </Card.Section>

    <Flex position="apart" mt="md" mb="xs">
      <Link href={article.url} target="_blank">
        <Text weight={500}>{article.title}</Text>
      </Link>
      <Badge color={article.sentiment_score > 0 ? 'green' : (article.sentiment_score < 0 ? 'red' : 'grey')} variant="light">
        {article.sentiment_score > 0 ? 'Positive' : (article.sentiment_score < 0 ? 'Negative' : 'Neutral')}
      </Badge>
    </Flex>

    <Text size="sm" color="dimmed">
      {article.content}
    </Text>

    <Accordion>
      <Accordion.Item label="Author" defaultOpened>
        <Text>{article.author}</Text>
      </Accordion.Item>
      <Accordion.Item label="Likes">
        <Flex align="center">
          <Text color="gray">{article.likes} likes</Text>
        </Flex>
      </Accordion.Item>
    </Accordion>

    <Button variant="light" color="blue" fullWidth mt="md" radius="md">
      Read more
    </Button>
  </Card>
);

export default ArticleCard;
