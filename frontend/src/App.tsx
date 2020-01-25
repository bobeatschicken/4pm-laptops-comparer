import React, { Suspense } from "react"
import { Router } from "@reach/router"
import Helmet from "react-helmet"

import { GlobalStyles } from "styles/globalStyles"

const LandingPage = React.lazy(() => import("pages/LandingPage"))

export const App: React.FC = () => {
  return (
    <>
      <Helmet>
        <title>Hello, world!</title>
      </Helmet>
      <GlobalStyles />
      <Suspense fallback={<></>}>
        <Router>
          <LandingPage path="/" />
        </Router>
      </Suspense>
    </>
  )
}

export default App
