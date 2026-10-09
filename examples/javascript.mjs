import { TikTokClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new TikTokClient({ apiKey });

  const search = await client.search({ keyword: "science" });
  console.log("search", search);
  const trending = await client.trending({  });
  console.log("trending", trending);
