
# GithubRepoScorer

This project uses the LangChain AI model to Score the Github Repositories of the given user.

## Demo



Uploading demo.mp4…




## Workflow

1. The project locates all of the repositories linked to the requested user and finding all files in the respective repositories that were created using C/C++, Python, or Java.The code that is found in those files is then retrieved, and it is added in a dictionary.
2. After that, pre-process the codes into small chunks and sends those chunks of code to OpenAI using Langchain's llm model querying for technical complexity evaluation.

3. After determining the average Technical Complexity of a specific repository, it predicts the most complex repository of a specific user.
## Instructions

1. After getting tokens from [Here](https://github.com/chayangirdhar/GithubRepoScorer/blob/main/README.md#api-reference) 

2. Add those token values to Sceret.py file as strings 

3. Run main.py file 
## API Reference

#### 



| Parameter | Type     |Description | Links            | 
| :-------- | :------- |:----------| :----------|
| `GithubAccessToken` | `string` |This is used to access repositories from the Github(you can access very few repositories from single IP without this). | [Get token from here](https://github.com/settings/tokens) |
| `OpenAI_api_key` | `string` |This is used to authorize and request the output from the OpenAI | [Get API from here](https://platform.openai.com/account/api-keys) |

#### 



## License

[MIT](https://choosealicense.com/licenses/mit/)

