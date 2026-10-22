use crawlora_tiktok::{Client, ModelTiktokSearchResponseDoc, TiktokSearchParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .tiktok
        .search(TiktokSearchParams {
            keyword: Some("science".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelTiktokSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
