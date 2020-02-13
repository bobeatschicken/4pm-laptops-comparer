import React, { HTMLAttributes } from "react"
import tw from "tailwind.macro"
import { FaPlus } from "react-icons/all"
import { Link } from "@reach/router"
import { Flipped } from "react-flip-toolkit"

const Wrapper = tw.div`
  m-4
  w-1/6 min-w-24 max-w-48
  flex-none
  text-white
`

const PageRect = tw.div`
  block
  relative
  pt-aspect-page
`

const SheetLayout = tw.div`
  absolute inset-0
  flex justify-center items-center
  bg-white
  shadow
  rounded
  text-4xl
  cursor-pointer
`

const InnerLayout = tw.div`
  absolute inset-0
  flex justify-center items-center
  border-dashed border-4 border-white
  rounded
  text-4xl
  cursor-pointer
`

const ProjectFooter = tw.div`
  mt-2
`

const NewProjectFooter = tw(ProjectFooter)`
  text-center
`

type DivProps = HTMLAttributes<HTMLDivElement>

type ProjectProps = {
  projectId: string
  projectName: string
}

// The thumbnail should not FLIP when transitioning from project overview to
// dashboard
function neverFlip() {
  return false
}

export const ProjectThumbnail: React.FC<ProjectProps & DivProps> = props => {
  const { projectId, projectName, ...otherProps } = props

  return (
    <Wrapper {...otherProps}>
      <PageRect as={Link} to={`/app/project/${projectId}`}>
        <Flipped flipId={`bg-${projectId}`} shouldFlip={neverFlip}>
          <SheetLayout />
        </Flipped>
      </PageRect>
      <ProjectFooter>
        {projectName}
      </ProjectFooter>
    </Wrapper>
  )
}

export const NewProjectThumbnail: React.FC<DivProps> = props => {
  const { onClick, ...otherProps } = props

  return (
    <Wrapper {...otherProps}>
      <PageRect onClick={onClick}>
        <InnerLayout>
          <FaPlus />
        </InnerLayout>
      </PageRect>
      <NewProjectFooter>
        New Workspace
      </NewProjectFooter>
    </Wrapper>
  )
}
