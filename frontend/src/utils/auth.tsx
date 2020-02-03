import React, { useState, useEffect, useCallback, useContext } from "react"

export const AuthContext = React.createContext<any>(undefined)

export const useAuth = () => useContext(AuthContext)

export const AuthProvider: React.FC = props => {
  const { children } = props

  return (
    <AuthContext.Provider value={null}>
      {children}
    </AuthContext.Provider>
  )
}
