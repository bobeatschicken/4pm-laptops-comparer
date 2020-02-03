import React from "react"
import tw from "tailwind.macro"
import { Flipped } from "react-flip-toolkit"

import richert from "images/richert.jpg"

const BrandImage = tw.img`
  mr-4
  w-12
  rounded-full
`

const Wrapper = tw.nav`
  flex items-center
  py-4 px-12
  text-white font-semibold
`

export const NavBar: React.FC = props => {
  return (
    <Wrapper>
      <Flipped flipId="richert">
        <BrandImage src={richert} />
      </Flipped>
      Comparé by Richert
    </Wrapper>
  )
}
