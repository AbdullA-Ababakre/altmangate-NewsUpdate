'use client'
/* eslint-disable */
import Image from 'next/image'
import { useMemo } from 'react'
import { LinkPreview } from '@dhaiwat10/react-link-preview'
// import json from './cluster_results.json'
import json from './cluster_results_15_2.json'

// const data = [
//   {
//     title: `OpenAI announces Sam Altman's departure`,
//     date: new Date('2023-11-17T00:00:00.000Z'),
//     description: `Chief technology officer Mira Murati appointed interim CEO to lead OpenAI; Sam Altman departs the company.`,
//     sources: ['https://openai.com/blog/openai-announces-leadership-transition'],
//   },
//   {
//     title: `Sam Altman writes the first tweet`,
//     description: `i loved my time at openai. it was transformative for me personally, and hopefully the world a little bit. most of all i loved working with such talented people.

//     will have more to say about what’s next later.`,
//     date: new Date('2023-11-17T11:46:00-08:00'),
//     sources: [
//       'https://twitter.com/sama/status/1725631621511184771',
//     ],
//   },
//   {
//     title: `OpenAI Co-Founder Altman Plans New Venture`,
//     description: `Sam Altman, the recently ousted CEO of OpenAI, has been telling investors that he is planning to launch a new venture, according to a person familiar with the matter. Former OpenAI president Greg Brockman is expected to join the effort and the project is still in development, the person said.`,
//     date: new Date('2023-11-18T13:46:00'),
//     sources: [
//       'https://www.theinformation.com/articles/openai-co-founder-altman-plans-new-venture',
//     ],
//   },
// ]

const data = json.map((item) => ({
  title: item.title,
  description: item.description.slice(0, 300) + '...',
  date: new Date(item.date),
  // sources: item.sources.slice(0, 5),
  sources: item.sources.slice(0, 3),
}))

const customFetcher = async (url: string) => {
  const response = await fetch(
    `https://rlp-proxy-hackathon-0aed409e764b.herokuapp.com/v2?url=${url}`
  )
  const json = await response.json()
  const { metadata } = json
  console.log(metadata)
  metadata.description = ''

  if (metadata.hostname.includes('x.com') || metadata.hostname.includes('twitter.com')) {
    metadata.title = metadata.title.slice(0, 100) + '...'
    metadata.image = 'https://static.dezeen.com/uploads/2023/07/x-logo-twitter-elon-musk_dezeen_2364_col_0-1.jpg'
  }
  return metadata
}

export default function Home() {
  const sortedData = useMemo(() => {
    return data.sort((a, b) => {
      return b.date.getTime() - a.date.getTime()
    })
  }, [data])
  return (
    <div>
      <div
        className="w-screen relative dark"
        style={{
          height: '50vh',
        }}
      >
        <Image
          alt="Altman Gate"
          src="/image.jpg"
          fill
          objectFit="cover"
          objectPosition="top"
        />
      </div>
      <main className="flex min-h-screen flex-col items-center pt-12 xl:pt-24 xl:px-24 px-12 gap-10">
        <h1 className="font-mono text-4xl">Altman Gate</h1>
        <p className="font-mono text-gray-200 max-w-3xl text-justify">
          On November 17, 2023, Sam Altman, co-founder of OpenAI, was removed as
          CEO and left the company's board. This decision came after a review by
          the board, which found Altman's lack of transparency impeded their
          oversight, leading to a loss of confidence in his leadership. But what
          happens next?
        </p>
        <section className="max-w-3xl mt-10">
          <ol className="relative border-s border-gray-200 dark:border-teal-500 pb-20">
            {sortedData.map((item, index) => (
              <li className="mb-10 ms-6" key={item.title}>
                <div className="absolute w-5 h-5 bg-gray-200 rounded-full mt-0.5 -start-2.5 border border-white dark:border-teal-500 dark:bg-teal-500" />
                <time className="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500 -mt-1">
                  {new Intl.DateTimeFormat('en-US', {
                    weekday: 'long', // e.g., Monday, Tuesday, etc.
                    year: 'numeric', // e.g., 2023
                    month: 'short', // e.g., January, February, etc.
                    day: 'numeric', // e.g., 1, 2, etc.
                    hour: 'numeric', // e.g., 1, 2, etc. (12-hour format by default)
                    minute: 'numeric', // e.g., 01, 02, etc.
                    second: 'numeric', // e.g., 01, 02, etc.
                    hour12: true, // Use 12-hour time format
                    timeZoneName: 'short', // Short time zone name (e.g., PST)
                  }).format(item.date)}
                </time>
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                  {item.title}
                </h3>
                <p className="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
                  {item.description}
                </p>
                {/* <a
                  href="#"
                  className="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-200 focus:text-blue-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-teal-500 dark:focus:ring-teal-500"
                >
                  Learn more{" "}
                  <svg
                    className="w-3 h-3 ms-2 rtl:rotate-180"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 14 10"
                  >
                    <path
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M1 5h12m0 0L9 1m4 4L9 9"
                    />
                  </svg>
                </a> */}
                <h2 className='text-gray-500 mb-2 mt-4 text-xs'>Sources</h2>
                <div className="grid grid-cols-3 gap-2">
                  {item.sources.map((source) => (
                    <a href={source} target='_blank'>
                      <LinkPreview
                        key={source}
                        borderColor="#111827"
                        fetcher={customFetcher}
                        url={source}
                        width="220px"
                        height="200px"
                        backgroundColor="#111827"
                        primaryTextColor="rgba(255,255,255,0.9)"
                        secondaryTextColor="rgb(156,163,175)"
                      />
                    </a>
                  ))}

                </div>
              </li>
            ))}
          </ol>
        </section>
      </main>
    </div>
  )
}
