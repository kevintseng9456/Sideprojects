import { gql } from '@apollo/client';

const GET_ISSUES = gql`
    query getIssues{
        getIssues{
            createdAt
            description
            title
            answer
            id
        }
    }
`

export {GET_ISSUES };