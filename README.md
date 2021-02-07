# YIT-V_Infrastructure

For use with the [Yodeling into the Void project](https://github.com/Han-Lon/YIT-V). This local
infrastructure is required to handle the public callback step in Twitter's 3-legged OAuth login process.

Refer to Twitter's documentation [here](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
for more info.

## To build new yitv_image
- `docker build -t yitv_image:Latest .`

## To deploy with wernight/ngrok
- Launch yitv_image normally from Docker Desktop
- Get the Docker-assigned container name
- Launch ngrok from Powershell with this command, replace "mystifying_fermat" with Docker-assigned container name from previous step
  - `docker run --rm -it --link mystifying_fermat wernight/ngrok ngrok http mystifying_fermat:5000`