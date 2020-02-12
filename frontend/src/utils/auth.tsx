import React, { useState, useMemo, useContext } from "react"
import { useGoogleLogin } from "react-google-login"

const noop = () => {}

type AuthContextValue =  {
  token: string
  signIn: () => void
}

export const AuthContext =
  React.createContext<AuthContextValue>(undefined as unknown as AuthContextValue)

export const useAuth = () => useContext(AuthContext)

export const AuthProvider: React.FC = props => {
  const { children } = props
  const [userObject, setUserObject] = useState()

  const { signIn, loaded } = useGoogleLogin({
    jsSrc: "https://apis.google.com/js/api.js",
    clientId: "58231025054-oua7h9662eqpb7ngl33qjhshetl13fod.apps.googleusercontent.com",
    scope: "profile email",
    accessType: "online",
    cookiePolicy: "single_host_origin",
    fetchBasicProfile: true,
    isSignedIn: true,
    uxMode: "popup",
    onRequest: noop,
    onFailure: console.error,
    onSuccess: setUserObject
  })

  const value = useMemo(() => ({
    token: userObject?.tokenId,
    signIn,
    loaded
  }), [loaded, signIn, userObject])

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  )
}
