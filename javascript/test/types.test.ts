import { TikTokClient } from "../src/index.js";

const client = new TikTokClient({ apiKey: "test-key" });
void client.videoComments({"aweme_id": "sample"});
void client.request("tiktok-video-comments", {"aweme_id": "sample"});
const streamResponse: Promise<Response> = client.request("tiktok-video-comments", {"aweme_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("tiktok-video-comments", {"aweme_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.videoComments({"aweme_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("tiktok-video-comments", {"aweme_id": "sample", "cursor": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("tiktok-video-comments", {"aweme_id": "sample"}, { responseType: "text" });
void rawText;


void client.category();
void client.request("tiktok-category");
// @ts-expect-error The selected operation requires its documented params.
void client.videoComments();
