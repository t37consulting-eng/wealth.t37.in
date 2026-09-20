# T37 Wealth (wealth.t37.in)

> Strategic wealth management, portfolio analytics, and advisory portal.

This project is configured for automated CI/CD deployment on **Vercel** connected directly to this **GitHub** repository.

## Architecture

- **Frontend**: Responsive HTML5, modern CSS3 with custom variables, and vanilla JavaScript.
  - Interactive Compound Interest & Investment Return Calculator
  - Institutional private wealth layout
- **Backend API**: Python 3.12 Serverless Function located at `/api/status.py`
  - Deploys automatically to Vercel's global edge network.
- **Deployment**: Automatic deployments on git push via Vercel GitHub integration.

## Local Development

You can run this project locally using Python or Node.js:

### Option 1: Using Python
```bash
python -m http.server 3000
```
Then visit `http://localhost:3000`.

### Option 2: Using Vercel CLI
```bash
vercel dev
```

## Vercel Deployment

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard).
2. Click **Add New...** > **Project**.
3. Select the `wealth.t37.in` repository.
4. If `wealth-t37-in` project name is already taken, give it an alternative name (such as `wealth-t37-app` or `wealth-t37-portal`).
5. Click **Deploy**.
