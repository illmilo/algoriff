<img src="website/static/logo.png" width=35px align=right>

# Django-Vercel-Neon

## Demo

[holytriangle.vercel.app](holytriangle.vercel.app)

## Description

This is a template repository that helps you to set up your Django+Vecel+Neon project.

## Setup
1. Use this repository as a template
2. Create project in Vercel using your new repository
3. [Integrate Neon into your new Vercel project]((https://vercel.com/illmilos-projects/~/integrations/neon))
4. ```bash
   git clone https://github.com/illmilo/ holytriangle
   cd holytriangle
   nano .env
   ```
5. Copy-paste Neon environmental variables from your Verel project into `.env` file
6. Cut `SECRET_KEY` from `settings.py` and paste it in `.env` key `SECRET_KEY`
7. Additionally, set up admin account with `ADMIN_LOGIN`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`. Otherwise, use default values:
    
    - Login: `admin`
    - Password: `securepassword123`

8. ```bash
   python3 manage.py migrate
   ```
Make sure `.env` is added to `.gitignore` and will not leak into production.

## License
This project is licensed under MIT License. Feel free to use this template. See [LICENSE](license) to learn more.