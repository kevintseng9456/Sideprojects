import Issue from '../models/Issue.js';

const reslovers = {
    Query:{
        async issue(_,{ID}) {
            return await Issue.findById(ID)
        },
        async getIssues(_,{amout}) {
            return await Issue.find().sort({createdAt: -1}).limit(amout)
        }
    },
    Mutation:{
        async createIssue(_, {issueInput: {title, description, answer}}){
            const createdIssue = new Issue({
                title: title,
                description: description,
                createdAt: new Date().toISOString(),
                answer: answer,
              });
              
              const res = await createdIssue.save();
              console.log(res._doc);
              return{
                id: res.id,
                ...res._doc
              }
        },
        async deleteIssue(_, {ID}){
            const wasDeleted = (await Issue.deleteOne({_id:ID})).deletedCount;
            return wasDeleted;
        },
        async editIssue(_, {ID, issueInput:{title, description,answer}}){
            const wasEdited = (await Issue.updateOne({_id:ID},{title: title, description: description, answer: answer})).modifiedCount;
            return wasEdited;
        }        
    }
}

export default reslovers;