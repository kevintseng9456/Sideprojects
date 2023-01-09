import { gql } from "apollo-server";

const typeDefs = gql`
type Issue{
    id: ID!
    title: String
    description: String
    createdAt: String
    answer: Boolean
}

input IssueInput {
    title: String
    description: String
    answer: Boolean
}

type Query{
    issue(ID: ID!): Issue!
    getIssues(amount: Int):[Issue]
}

type Mutation{
    createIssue(issueInput: IssueInput):Issue!
    deleteIssue(ID: ID!): Boolean
    editIssue(ID: ID!, issueInput: IssueInput): Issue!
}
`
export default typeDefs;