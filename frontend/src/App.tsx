import React, { Suspense } from "react"
import { Router, Location } from "@reach/router"
import Helmet from "react-helmet"
import { Flipper } from "react-flip-toolkit"

import { GlobalStyles } from "styles/globalStyles"
import { AuthProvider } from "utils/auth"

import LandingPage from "pages/LandingPage"
import LoginPage from "pages/LoginPage"
import Dashboard from "pages/Dashboard"
import ProjectOverview from "pages/ProjectOverview"

export const App: React.FC = () => {
  return (
    <>
      <Helmet>
        <title>Hello, world!</title>
      </Helmet>
      <GlobalStyles />
      <AuthProvider>
        <Location>
          {({ location }) => (
            <Flipper flipKey={location}>
              <Suspense fallback={<></>}>
                <Router>
                  <LandingPage path="/" />
                  <LoginPage path="/app/login" />
                  <Dashboard path="/app/first" />
                  <ProjectOverview path="/app/project/:projectId" />
                </Router>
              </Suspense>
            </Flipper>
          )}
        </Location>
      </AuthProvider>
    </>
  )
}

export default App
