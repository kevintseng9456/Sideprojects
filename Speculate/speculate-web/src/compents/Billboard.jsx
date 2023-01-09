import React from 'react'
import APIs from '../APIs'
// import { useMutation } from '@apollo/client';

function Billboard(props) {
  const getIssues = APIs().getIssues; //抓取getIssues的屬性值
  const { createIssue, deleteIssue, editIssue } = APIs();

  // 使用這些操作
  async function handleCreateButtonClick() {
    await createIssue({ title: '新增的標題', description: '新增的描述' });
    }
    
  async function handleDeleteButtonClick() {
  await deleteIssue('要刪除的議題的 ID');
  }
  
  async function handleEditButtonClick(issueID, answer) {
    await editIssue(issueID, answer);

  }
        

  const handleYesButtonClick = (issueId) => {
    handleEditButtonClick(issueId,true);
  }
  
  const handleNoButtonClick = (issueId) => {
    handleEditButtonClick(issueId, false);
  }    
    
  return (
    <div className='w-screen h-screen bg-primary flex items-start justify-center pt-[8vh]'>
        <div className=' bg-secondary my-10 w-[70vh] h-[60vh]'>
            <div className='w-full h-full'>
                <p className='w-full h-full flex items-center justify-center text-center text-text_m sm:text-6xl lg:text-7xl text-6xl'>
                  {/* 宗教是一種品牌嗎? */}
                  {getIssues && getIssues.map(issue => (
                    <div key={issue.id}>
                      <p>{issue.title}</p>
                    </div>
                  ))}
                </p> 
            </div>
            <div >
            {getIssues && getIssues.map(issue => (
              <div key={issue.id} className='flex items-center justify-center space-x-0 pt-5'>
                <button onClick={() => handleYesButtonClick(issue.id)} className='text-text_m sm:text-6xl lg:text-7xl text-6xl w-full bg-pink-600'>YES</button>
                <button onClick={() => handleNoButtonClick(issue.id)} className='text-text_m sm:text-6xl lg:text-7xl text-6xl w-full bg-lime-600'>NO</button>
              </div>
              ))}
            </div>

        </div>
    </div>
  )
}

export default Billboard
