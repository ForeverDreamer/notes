# Adding synonyms

## Creating index with custom analyzer

```
PUT /synonyms
{
  "settings": {
    "analysis": {
      "filter": {
        "synonym_test": {
          "type": "synonym", 
          "synonyms": [
            "awful => terrible",  # awful被替换成terrible
            "awesome => great, super",  # awesome被同时替换成great和super，两者位于同一个position
            "elasticsearch, logstash, kibana => elk",  # elasticsearch, logstash, kibana都被替换成elk
            "weird, strange"  # 两者被放在同一个position，没有替换操作
          ]
        }
      },
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "synonym_test"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "my_analyzer"
      }
    }
  }
}
```

## Testing the analyzer (with synonyms)

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "awesome"
}
```

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "Elasticsearch"
}
```

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "weird"
}
```

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "Elasticsearch is awesome, but can also seem weird sometimes."
}
```

## Adding a test document

```
POST /synonyms/_doc
{
  "description": "Elasticsearch is awesome, but can also seem weird sometimes."
}
```

## Searching the index for synonyms

```
GET /synonyms/_search
{
  "query": {
    "match": {
      "description": "great"
    }
  }
}
```

```
GET /synonyms/_search
{
  "query": {
    "match": {
      "description": "awesome"
    }
  }
}
```