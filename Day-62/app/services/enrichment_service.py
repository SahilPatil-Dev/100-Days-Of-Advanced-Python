from app.integrations.external_api import fetch_external_data


async def enrich_data_with_external(log_data):

    external_data = await fetch_external_data()

    # simple simulation: attach metadata
    enriched = []

    for i, row in enumerate(log_data):
        row["external_info"] = external_data[i % len(external_data)]["name"]
        enriched.append(row)

    return enriched