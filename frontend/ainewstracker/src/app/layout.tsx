import './globals.css'
import Head from 'next/head'
import { Inter } from 'next/font/google'
import PropTypes from 'prop-types'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'AINewsTracker',
  description: 'A web application for backtesting the influence of financial news on the stock market using AI.',
}

function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div>
      <Head>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet" />
      </Head>
      <body>{children}</body>
    </div>
  )
}

RootLayout.propTypes = {
  children: PropTypes.node.isRequired,
}
export default RootLayout;