# Call-of-Project matching_and_recommendation_service
**Author:** [Emir KAFADAR](https://github.com/EmirKafadar)

Due to insufficient data, we didn't use machine learning and artificial intelligence for this project. Instead, we utilized the Python set data structure to suggest projects to users and to match them with each other. However, if the **Call-of-Project** project grows and we have enough data, we might consider incorporating machine learning and AI.

The **Call-of-Project** project connects to this service using a **feign-client** to retrieve the necessary IDs (matching user IDs and suggested project IDs). It then transforms the projects within its system into a format that users can see. This information is then delivered to users via email at specific times and days of the week, using a **scheduler service**.

## Architecture   
- ![dark](https://github.com/CallOfProject/UserMatching-Suggestion/assets/79942350/34aca9ea-6bc7-4a74-90be-ac0802864509)
- **This diagram shows how the match-and-recommendation service interacts with the Call-of-Project project.**

## Example Emails
- **Project Recommendation**
  - ![project_recommendation](https://github.com/CallOfProject/UserMatching-Suggestion/assets/79942350/2ce568fb-dffd-429c-82ae-dfaa83393757)

- **User Matching:**
  - ![user_match](https://github.com/CallOfProject/UserMatching-Suggestion/assets/79942350/b82847c3-2b46-4055-893e-fc47f42ec90f)
